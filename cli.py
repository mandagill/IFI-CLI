import click

@click.group()
def cli():
	pass

@click.command()
@click.option('--input-folder', required=True)
@click.option('--output-folder', required=True)
def makesip(input_folder, output_folder):
	click.echo(f"You would like to make a SIP with this input: {input_folder} and this output: {output_folder}")

@click.command()
def makeaip():
	click.echo('You would like to make an AIP!')

cli.add_command(makesip)
cli.add_command(makeaip)

if __name__ == '__main__':
    cli()