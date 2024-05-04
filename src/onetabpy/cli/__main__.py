import importlib.metadata as metadata
from importlib import import_module

import click

from onetabpy.config.log_config import logger


__version__ = metadata.version("onetabpy")


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    epilog="For more information, see the documentation at https://github.com/jimbrig/onetabpy/docs",
)
@click.version_option(version=__version__)
@click.pass_context
def onetabpy(ctx, **kwargs):
    """OneTabPy: Backup and restore your OneTab tabs."""
    logger.info("OneTabPy CLI invoked with (version=%s)", __version__)

    if ctx.invoked_subcommand is None:
        logger.info("No subcommand invoked. Exiting.")
        click.echo("No subcommand invoked. Exiting.")
        ctx.exit(0)


@onetabpy.command(name="backup")
@click.pass_context
def backup(ctx, **kwargs):
    """Backup your OneTab tabs."""
    logger.info("Backup command invoked.")
    click.echo("Backing up OneTab tabs...")
    runner = import_module("onetabpy.backup")
    runner.backup_onetab()


@onetabpy.command(name="restore")
@click.argument("index", type=int)
@click.pass_context
def restore(ctx, index, **kwargs):
    """Restore your OneTab tabs."""
    logger.info("Restore command invoked.")
    click.echo(f"Restoring OneTab tabs from backup ID {index}...")
    runner = import_module("onetabpy.restore")
    runner.restore_onetab(index)
