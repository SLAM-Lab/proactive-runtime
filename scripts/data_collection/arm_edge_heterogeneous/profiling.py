#!/usr/bin/env python3

import os
import time

if __name__ == "__main__":
    benchmarks = [
                500, 502, 505, 520, 523, 525, 531, 541, 548, 557,
                503, 507, 508, 510, 511, 519, 521, 527, 538, 544, 549, 554]
    perf_events = [
                "instructions,cpu-cycles",
                "instructions,armv8_pmuv3/stall_backend/",
                "instructions,armv8_pmuv3/stall_frontend/",
                "instructions,armv8_pmuv3/br_mis_pred/",
                "instructions,armv8_pmuv3/br_pred/",
                "instructions,armv8_pmuv3/br_retired/",
                "instructions,armv8_pmuv3/inst_spec/",
                "instructions,armv8_pmuv3/inst_retired/",
                "instructions,armv8_pmuv3/l1d_cache/",
                "instructions,armv8_pmuv3/l1d_cache_refill/",
                "instructions,armv8_pmuv3/l1d_cache_wb/",
                "instructions,armv8_pmuv3/l1d_tlb/",
                "instructions,armv8_pmuv3/l1d_tlb_refill/",
                "instructions,armv8_pmuv3/l1i_cache/",
                "instructions,armv8_pmuv3/l1i_cache_refill/",
                "instructions,armv8_pmuv3/l1i_tlb/",
                "instructions,armv8_pmuv3/l1i_tlb_refill/",
                "instructions,armv8_pmuv3/l2d_cache/",
                "instructions,armv8_pmuv3/l2d_cache_allocate/",
                "instructions,armv8_pmuv3/l2d_cache_refill/",
                "instructions,armv8_pmuv3/l2d_cache_wb/",
                "instructions,armv8_pmuv3/l2d_tlb/",
                "instructions,armv8_pmuv3/l2d_tlb_refill/",
                "instructions,armv8_pmuv3/l3d_cache/",
                "instructions,armv8_pmuv3/l3d_cache_allocate/",
                "instructions,armv8_pmuv3/l3d_cache_refill/",
                "instructions,armv8_pmuv3/l3d_cache_wb/",
                "instructions,armv8_pmuv3/mem_access/"
                ]

    for benchmark in benchmarks:
        count = 0
        for events in perf_events:
            command  = "taskset --cpu-list 0"
            command += ' perf stat -I 10'
            command += ' -e ' + str(events)
            command += ' -o arm_edge_InO_1.5GHz_' + str(benchmark) + '_' + str(count)
            command += ' -x,'
            command += " runcpu --config=matthew-1cpu " + str(benchmark)
            print(command)
            count += 1

    for benchmark in benchmarks:
        count = 0
        for events in perf_events:
            command  = "taskset --cpu-list 4"
            command += ' perf stat -I 10'
            command += ' -e ' + str(events)
            command += ' -o arm_edge_OOO_1.5GHz_' + str(benchmark) + '_' + str(count)
            command += ' -x,'
            command += " runcpu --config=matthew-1cpu " + str(benchmark)
            print(command)
            count += 1

    for benchmark in benchmarks:
        count = 0
        for events in perf_events:
            command  = "taskset --cpu-list 7"
            command += ' perf stat -I 10'
            command += ' -e ' + str(events)
            command += ' -o arm_edge_OOO_cache_1.5GHz_' + str(benchmark) + '_' + str(count)
            command += ' -x,'
            command += " runcpu --config=matthew-1cpu " + str(benchmark)
            print(command)
            count += 1



