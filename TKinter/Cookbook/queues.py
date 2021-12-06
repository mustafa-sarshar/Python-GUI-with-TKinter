def write_to_scrolled_text(inst, n_q_to_show):
    print(f"Hi From Queue {inst}")
    inst.create_thread(num_of_queues_to_show=n_q_to_show)