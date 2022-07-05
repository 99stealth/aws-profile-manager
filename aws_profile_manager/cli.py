import os
import sys
import click
import logging

from aws_profile_manager._version import __version__

def setup_logging(quiet: bool):
    ''' Function is setting logging configuration '''

    if quiet:
        logging_level = logging.WARNING
    else:
        logging_level = logging.INFO
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
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
        except FileNotFoundError:
            print("Command not found")
            return
        return ns['cli']

class RootFlags(object):
    def __init__(self, quiet=None) -> None:
        self.quiet = quiet

@click.group(cls=MyCLI, help='This tool\'s subcommands are loaded from a plugin folder dynamically.')
@click.pass_context
@click.version_option(__version__)
@click.option('-q', '--quiet', help='Less outputs', type=bool, is_flag=True, required=False, default=False)
def cli(ctx, quiet):
    ctx.obj = RootFlags(quiet)
    setup_logging(quiet=quiet)

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        logging.error("\nProcess has been stopped. Interrupted by user")
        sys.exit(1)