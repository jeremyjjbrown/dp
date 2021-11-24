import click
import json

from dpctl.config import Config
from dpctl.workflow import Workflow


@click.group()
@click.option('-v', '--debug/--no-debug', default=False)
@click.option('-c', '--config', default='dpctl.yaml')
@click.pass_context
def cli(ctx, debug, config):
    if debug:
        click.echo("Debug mode is enabled.")
    ctx.obj = {}
    ctx.obj['config'] = Config(configPath=config)
    ctx.obj['workflow'] = Workflow(ctx.obj['config'])


@cli.command()
@click.pass_context
def apply(ctx):
    results = ctx.obj['workflow'].apply()
    click.echo(f'apply results: {results}')


@cli.command()
def plan():
    click.echo('run plan')
    click.echo(json.dumps(ctx.obj['config'], indent=2, default=str))


@cli.command()
def delete():
    click.echo('run delete')


@cli.command()
def vet():
    click.echo('run vet')


@cli.command()
def lint():
    click.echo('run lint')


if __name__ == '__main__':
    cli()
