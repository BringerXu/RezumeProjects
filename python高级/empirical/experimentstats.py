import pstats
p = pstats.Stats('profile1')
p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('calls').print_stats(10)
p.sort_stats('cumulative').print_stats(10)
p.sort_stats('time').print_stats(10)