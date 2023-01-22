# Third Party
import click


@click.group()
def controller():
    pass

@controller.command()
def train_valid():
    pass

@controller.command()
def valid():
    pass

@controller.command()
def submission():
    pass

if __name__ == "__main__":
    controller()
