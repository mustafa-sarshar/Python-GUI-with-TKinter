
import sys
import tkinter as tk
from tkinter import ttk, filedialog
from pathlib import Path
import pandas as pd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
matplotlib.use("TkAgg")

# In[] Global Variables and Constants
style.use("ggplot")
WINDOW_SIZE = (640, 600)
LARGE_FONT= ("Verdana", 12)
NORMAL_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)
skip_rows_n = 0
features_to_plot = []
feature_to_work_on = ""
labeled_feature = ""
# Define variables for the df
df_address_to_open = Path("files", "file_demo.csv")
df_address_to_save = Path("files", "file_demo.csv")
df = pd.DataFrame()
df = pd.read_csv(df_address_to_open, skiprows=int(skip_rows_n))

# In[] Global Functions
def set_features_to_plot():
    def set_features(feats):
        global features_to_plot, fig, axs, line_main, line_mask, line_labels
        features_to_plot = feats.split(", ")
        print("Features to plot set to: ", features_to_plot)
        # Plot the graph
        axs.clear()
        axs.set_title(f"Labeling '{df_address_to_open.name}' for '{labeled_feature}' feature", loc="center")
        *line_main, = axs.plot(list(df.index), df.loc[:, features_to_plot])
        line_mask, = axs.plot(df[feature_to_work_on], "rs-")
        line_mask.set_alpha(0.0)
        line_labels, = axs.plot(list(df.index), df[f"{feature_to_work_on}_{labeled_feature}"], "gs-", linewidth=1)
        line_labels.set_alpha(0.0)
        fig.canvas.draw()
    # Design the window
    popup = tk.Tk()
    popup.wm_title("Set features to plot")
    popup.resizable(False, False)
    label = ttk.Label(popup, text="Skip rows:", font=NORMAL_FONT, justify=tk.CENTER)
    label.grid(row=0, column=0)
    entry_features = tk.Entry(popup, justify=tk.CENTER, state=tk.NORMAL, font=NORMAL_FONT)
    entry_features.grid(row=0, column=1)
    btn_open = ttk.Button(popup, text="Set", command=lambda: set_features(entry_features.get()))
    btn_open.grid(row=1, column=0)
    popup.mainloop()

def open_file(object):
    def open_file_window(skiprows_n, feat_to_work_on, label_feature):
        global df, df_address_to_open, skip_rows_n, feature_to_work_on, features_to_plot, labeled_feature, \
            fig, axs, line_main, line_mask, line_labels, \
            x_from, x_to
        # Open the file browser
        tk.Tk.filename = filedialog.askopenfilename(
            initialdir=df_address_to_open.parent,
            title="Select a file please...",
            filetypes=(("Comma-separated values file", "*.csv"), ("any file type", "*.*"))
        )
        if tk.Tk.filename != "":
            df_address_to_open = Path(tk.Tk.filename)
            skip_rows_n = skiprows_n
            feature_to_work_on = feat_to_work_on
            features_to_plot = [feature_to_work_on]
            labeled_feature = label_feature
            print("features_to_plot", features_to_plot, "feature_to_work_on", feature_to_work_on)
            x_from, x_to = 0, len(df)
            print(df_address_to_open.name)
            print("df Address to open: ", df_address_to_open)
            df = pd.read_csv(df_address_to_open, skiprows=int(skip_rows_n))
            df[f"{feature_to_work_on}_{labeled_feature}"] = list([0] * len(df))
            print("len(df): ", len(df))
            # Plot the graph
            fig = Figure(dpi=100)
            axs = fig.add_subplot(111)
            axs.set_autoscale_on(True)
            axs.autoscale_view(tight=True, scalex=True, scaley=True)
            axs.set_title(f"Labeling {df_address_to_open.name} on {feature_to_work_on}", loc="center")
            *line_main, = axs.plot(list(df.index), df.loc[:, ["Gyr_Z", "Gyr_X"]])
            line_mask, = axs.plot(df[feature_to_work_on], "rs-")
            line_mask.set_alpha(0.0)
            line_labels, = axs.plot(list(df.index), df[f"{feature_to_work_on}_{labeled_feature}"], "gs-", linewidth=1)
            line_labels.set_alpha(0.0)
            canvas = FigureCanvasTkAgg(fig, object)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            graph_toolbar = NavigationToolbar2Tk(canvas, object)
            graph_toolbar.update()
            # Define functions to detect clicking
            def onButtonPress(event):
                global x_from
                if (event.xdata) and (event.ydata):
                    x_from = event.xdata
                    print(f"From: {x_from} to {x_to}")
            def onButtonReleased(event):
                global x_to
                if (event.xdata) and (event.ydata):
                    x_to = event.xdata
                    print(f"From: {x_from} to {x_to}")
            fig.canvas.mpl_connect("button_press_event", onButtonPress)
            fig.canvas.mpl_connect("button_release_event", onButtonReleased)
     # Design the window
    popup = tk.Tk()
    popup.wm_title("Open a File")
    popup.resizable(False, False)
    label = ttk.Label(popup, text="Skip rows:", font=NORMAL_FONT, justify=tk.CENTER)
    label.grid(row=0, column=0)
    entry_skiprows = tk.Entry(popup, justify=tk.CENTER, state=tk.NORMAL, font=NORMAL_FONT)
    entry_skiprows.grid(row=0, column=1)
    label_2 = ttk.Label(popup, text="Feature to work on:", font=NORMAL_FONT, justify=tk.CENTER)
    label_2.grid(row=1, column=0)
    entry_feature_to_work_on = tk.Entry(popup, justify=tk.CENTER, state=tk.NORMAL, font=NORMAL_FONT)
    entry_feature_to_work_on.grid(row=1, column=1)
    label_3 = ttk.Label(popup, text="Label Feature:", font=NORMAL_FONT, justify=tk.CENTER)
    label_3.grid(row=2, column=0)
    entry_label_feature = tk.Entry(popup, justify=tk.CENTER, state=tk.NORMAL, font=NORMAL_FONT)
    entry_label_feature.grid(row=2, column=1)
    btn_open = ttk.Button(popup, text="Open",
                          command=lambda: open_file_window(
                              int(entry_skiprows.get()),
                              entry_feature_to_work_on.get(),
                              entry_label_feature.get())
    )
    btn_open.grid(row=3, column=0)
    center_x, center_y = 100, 200
    popup.geometry(f"+{center_x}+{center_y}")
    popup.mainloop()
def save_file():
    global df, df_address_to_save, df_address_to_open
    # Open the file browser
    tk.Tk.filename = filedialog.asksaveasfilename(
        initialdir=df_address_to_save.parent,
        initialfile=df_address_to_open.name,
        title="Enter the file name please...",
        filetypes=(("Comma-separated values file", "*.csv"), ("any file type", "*.*"))
    )
    df_address = tk.Tk.filename
    if df_address != "":
        try:
            pd.DataFrame.to_csv(df, df_address)
            df_address_to_save = Path(df_address)
            print("df saved in: ", df_address_to_save)
        except ValueError:
            print(f"Error {ValueError} occured!!! Please try again!!!")

# In[] Main App
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        global df
        tk.Tk.__init__(self, *args, **kwargs)
        # Styling
        self.app_styling()
        # Appearance
        self.app_init_appearance()
        # Define the container of the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Define the menus
        menubar = tk.Menu(container)
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File", command=lambda: open_file(self))
        file_menu.add_command(label="Save File", command=save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=file_menu)
        # Graph Menu
        graph_menu = tk.Menu(menubar, tearoff=0)
        graph_menu.add_command(label="Features to plot", command=set_features_to_plot)
        menubar.add_cascade(label="Graph", menu=graph_menu)
        # Other Menu
        others_menu = tk.Menu(menubar, tearoff=0)
        others_menu.add_command(label="DF length", command=lambda: print(len(df)))
        others_menu.add_command(label="DF cols", command=lambda: print(df.columns.to_list()))
        menubar.add_cascade(label="Others", menu=others_menu)
        # Add all the menus to the menubar
        tk.Tk.config(self, menu=menubar)
        # Initialize the frames
        self.frames = {}
        for F in (StartPage, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def app_styling(self):
        tk.Tk.wm_title(self, "Main App")

    def app_init_appearance(self):
        settings = sys.argv
        if len(settings) > 1:
            if "-fullscreen" in settings:
                self.attributes("-fullscreen", True)
            elif "-maximize" in settings:
                screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
                # set the position of the window to the center of the screen
                self.geometry(f"{screen_width}x{screen_height}+0+0")
            elif "-centered" in settings:
                window_width = WINDOW_SIZE[0]
                window_height = WINDOW_SIZE[1]
                # get the screen dimension
                screen_width = self.winfo_screenwidth()
                screen_height = self.winfo_screenheight()
                # find the center point
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)
                # set the position of the window to the center of the screen
                self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        else:
            self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# In[] Run the App
app = MainApp()
app.mainloop()