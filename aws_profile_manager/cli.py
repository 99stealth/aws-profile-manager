import os
import sys
import click
import logging

def setup_logging(quiet: bool, verbose: bool):
    ''' Function is setting logging configuration '''

    if verbose:
        logging_level = logging.INFO
    elif quiet:
        logging_level = logging.ERROR
    else:
        logging_level = logging.WARNING
    logging.basicConfig(format='%(message)s', level=logging_level)

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.startswith('_'):
                continue
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')

if __name__ == '__main__':
    try:
        setup_logging(quiet=False, verbose=False)
        cli()
    except KeyboardInterrupt:
        logging.error("\nProcess has been stopped. Interrupted by user")
        sys.exit(1)