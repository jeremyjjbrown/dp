import click
import json

from dpctl.config import Config


@click.group()
@click.option('-v', '--debug/--no-debug', default=False)
@click.option('-c', '--config', default='dpctl.yaml')
@click.pass_context
def cli(ctx, debug, config):
    if debug:
        click.echo("Debug mode is enabled.")
    ctx.obj = Config(configPath=config)
    click.echo(json.dumps(ctx.obj, indent=2, default=str))


@cli.command()
def apply():
    click.echo('run apply')


@cli.command()
def plan():
    click.echo('run plan')


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
