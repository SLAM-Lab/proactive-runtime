#!/usr/bin/env python3

import os
import time

if __name__ == "__main__":
    benchmarks = [
                500, 502, 505, 520, 523, 525, 531, 541, 548, 557,
                503, 507, 508, 510, 511, 519, 521, 527, 538, 544, 549, 554]
    perf_events = [
        "instructions,cpu-cycles,br_pred,br_mis_pred",
        "instructions,l1d_cache_rd,l1d_cache_wr,l1d_cache",
        "instructions,l1i_cache,l1i_cache_refill,remote_access",
        "instructions,l2d_cache_rd,l2d_cache_wr,l2d_cache",
        "instructions,l1d_tlb,l1d_tlb_rd,l1d_tlb_wr",
        "instructions,dtlb_walk,itlb_walk,l1i_tlb",
        "instructions,l2d_tlb,l2d_tlb_rd,l2d_tlb_wr",
        "instructions,vfp_spec,inst_spec,ase_spec",
        "instructions,stall_backend,stall_frontend,ll_cache_miss_rd",
        "instructions,mem_access,mem_access_rd,mem_access_wr",
    ]

    sample_period = [10]
    cpus = [0]
    freqs = ['1.50GHz']

    for cpu in cpus:
        for freq in freqs:
            for epoch in sample_period:
                for benchmark in benchmarks:
                    for events in perf_events:
                        command  = "taskset --cpu-list " + str(cpu)
                        command += ' perf stat -I ' + str(epoch)
                        command += ' -e ' + str(events)
                        command += ' -o cpu_' + str(cpu) + '_freq_' + str(freq) + '_epoch_' + str(epoch) + '_' + str(benchmark) + '_' + str(events)
                        command += ' -x,'
                        command += " runcpu --config=matthew-1cpu " + str(benchmark)
                        print(command)

