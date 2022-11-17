def Convert_Ist_to_Imt(Ist, i, j):
    # @Ist: A single-thread input
    # @i, @j: an index of racing syscalls within Ist

    # Get two threads, thr0 and thr1
    thr0 = get_thread()
    thr1 = get_thread()

    # Assign syscalls to thr0 and thr1
    syscalls = get_syscalls(Ist)
    thr0.add_syscalls(syscalls[: i + 1])
    thr1.add_syscalls(syscalls[i + 1 :])

    Imt = Construct_Imt(thr0, thr1)
    return Imt
