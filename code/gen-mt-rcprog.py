def Convert_Pst_to_Pmt(Pst, i, j, RP_i, RP_j):
    # @Pst: A singled threaded program (annotated)
    # @i, @j: an index of racing syscalls within Pst
    # @RP_i, @RP_j: an address of a corresponding racepair
    # instruction (to syscalls[i] and syscalls[j], respectively)

    # Get pinned threads, thr0 and thr1
    thr0 = get_pinned_thread(vCPU0)
    thr1 = get_pinned_thread(vCPU1)

    # Assign syscalls to thr0 and thr1
    syscalls = get_syscalls(Pst)
    thr0.add_syscalls(syscalls[:i])
    thr1.add_syscalls(syscalls[i+1:j])

    # Determine the execution order
    r = random([vCPU0, vCPU1])
    thr0.add_hypercall(hcall_order(r))

    # Trigger and check races
    thr0.add_hypercall(hcall_set_bp(vCPU0, RP_i))
    thr0.add_syscalls(syscalls[i])
    thr0.add_hypercall(hcall_check-race())

    thr1.add_hypercall(hcall_set_bp(vCPU1, RP_j))
    thr1.add_syscalls(syscalls[j])
    thr1.add_hypercall(hcall_check_race())

    # Post-race behaviors
    thr0.add_syscalls(gen_random_syscalls())
    thr1.add_syscalls(gen_random_syscalls())

    Pmt = Construct_Pmt(thr0, thr1)
    return Pmt
