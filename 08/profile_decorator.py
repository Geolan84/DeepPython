"""Profile decorator for profiling functions."""
import cProfile
import pstats
import io


class profile_deco:

    def __init__(self, function):
        self.prof = cProfile.Profile()
        # Set new attribute.
        self.function = function

    def __call__(self, *args, **kwargs):
        self.prof.runcall(self.function, *args, **kwargs)

    def print_stat(self):
        """Prints cummulative statistics about function."""
        s = io.StringIO()
        ps = pstats.Stats(self.prof, stream=s).sort_stats("cumulative")
        ps.print_stats()
        print(s.getvalue())


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


add(1, 2)
add(4, 5)
sub(4, 5)

add.print_stat()
sub.print_stat()
