#!python
import click

@click.group('cli')
def cli():
    """Interface to ETL Module Production Database"""


@cli.command()
def db_reset():
    from db import session
    from db.models import Base

    # Modifies the drop tables sqlalchemy command to append CASCADE
    from sqlalchemy.schema import DropTable
    from sqlalchemy.ext.compiler import compiles

    @compiles(DropTable, "postgresql")
    def _compile_drop_table(element, compiler, **kwargs):
        return compiler.visit_drop_table(element) + " CASCADE"

    with session() as session, session.begin():
        Base.metadata.drop_all(session.bind)
        Base.metadata.create_all(session.bind)


@cli.command()
@click.argument('username')
@click.argument('password')
@click.argument('email')
@click.option('--affiliation', default="None")
def user_create(username, password, email, affiliation):
    from db import session
    from db.models import User
    with session() as session, session.begin():
        user = User.new(username, password, email, affiliation)
        session.add(user)
        print(f"Added new User: {user}")


@cli.command()
@click.argument('username')
@click.option('--deactivate', is_flag=True)
def user_activate(username, deactivate):
    from db import session
    from db.models import User
    with session() as session, session.begin():
        user = session.query(User).where(User.username == username).one_or_none()
        if user is None:
            print(f"User {username} not found.")
            return
        if deactivate:
            user.is_active = False
        else:
            user.is_active = True

@cli.command()
def user_list():
    from db import session
    from db.models import User
    with session() as session, session.begin():
        users = session.query(User).all()
        click.echo(f"{'ID':<5s}|{'Username':>15s}|{'Email Address':>20s}|{'Is Active':>12s}")
        click.echo("-"*52)
        for user in users:
            click.echo(f"{user.id:<5d}|{user.username:>15s}|{user.email:>20s}|{user.is_active:12}")


if __name__ == '__main__':
    cli()