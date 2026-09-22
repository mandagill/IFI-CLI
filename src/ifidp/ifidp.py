import click

@click.group()
def cli():
	pass


@click.command()
@click.option('--input-folder', '-i', required=True, multiple=True)
@click.option('--output-folder', '-o', required=True, multiple=True)
@click.option('--supplement', '-s')
@click.option('--easy-dcp-report', '-edcp')
def makesip(input_folder, output_folder, supplement, easy_dcp_report):
	"""Command requires one or more input folders and one or more output folders. The input is captured as a tuple.

	This function should 1. delegate calls to helper functions while 2. logging each call to the helper in the created logfile and 3. use the logfile to resume packaging if the script fails at some point in package creation"""

	click.echo(f"""You would like to make a SIP with this input: {input_folder} and this output: {output_folder}\n
		the argument is of type: {type(input_folder)}""")


@click.command()
def makeaip():
	click.echo('You would like to make an AIP!')


@click.command()
def validate_package():
	# TODO implement a function that automates the manual steps taken in step 4 of the DCP workflow. It should take a directory location as arg and return either "true" or a list of items to rectify before SIPping can take place
	pass


@click.command()
def make_folder():
	# TODO make a command that prompts the user to enter the necessary information to create a folder that adheres to IFI naming conventions.
	# ALTERNATIVELY, create a .csv with the relevant info and allow the script to read that file and make the folder per naming conventions for you?
	pass


#Possible other flags: for 

cli.add_command(makesip)
cli.add_command(makeaip)

if __name__ == '__main__':
    cli()