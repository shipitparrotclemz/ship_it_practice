import psycopg2
from psycopg2._psycopg import cursor


class PirateParrot:
    """
    A data model representing a Pirate Parrot
    """

    def __init__(self, name: str, weapon: str):
        self.name = name
        self.weapon = weapon

    def __str__(self) -> str:
        return f"{self.name} has a {self.weapon}"


class PirateParrotDAO:
    def __init__(
        self,
        database: str = "pirate_database",
        user: str = "",
        password: str = "",
        host: str = "localhost",
        port: int = 5432,
    ):
        self.database_connector = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port
        )

    def get_all_pirate_parrots(self) -> list[PirateParrot]:
        # Create a cursor to execute queries
        my_pirate_cursor: cursor = self.database_connector.cursor()

        # execute a query to get all the pirate parrots
        # this loads the results into the cursor
        my_pirate_cursor.execute(query="SELECT name, weapon FROM pirate_parrots")

        # fetch all results from the cursor
        rows: list[tuple[str]] = my_pirate_cursor.fetchall()
        pirate_parrots: list[PirateParrot] = []

        # for each row, create a PirateParrot object and add it to the list
        for row in rows:
            pirate_name: str = row[0]
            pirate_weapon: str = row[1]
            pirate_parrot: PirateParrot = PirateParrot(
                name=pirate_name, weapon=pirate_weapon
            )
            pirate_parrots.append(pirate_parrot)
        return pirate_parrots

    def insert_pirate_parrot(self, pirate_parrot: PirateParrot) -> None:
        # Create a cursor to execute queries
        cursor = self.database_connector.cursor()

        # execute an INSERT to add a pirate parrot to the database
        # this is not executed till we commit the changes
        cursor.execute(
            "INSERT INTO pirate_parrots (name, weapon) VALUES (%s, %s)",
            (pirate_parrot.name, pirate_parrot.weapon),
        )
        # commit the INSERT to the database
        self.database_connector.commit()


if __name__ == "__main__":
    # initialize the PirateParrotDAO
    # this is the object that will be used to interact with the database
    pirate_parrot_dao: PirateParrotDAO = PirateParrotDAO()

    # create a pirate parrot object, ready to be inserted into the database
    my_first_parrot: PirateParrot = PirateParrot(
        name="Captain Jack Sparrow", weapon="Cutlass"
    )

    # insert the pirate parrot to the database
    pirate_parrot_dao.insert_pirate_parrot(pirate_parrot=my_first_parrot)

    # we should be able to get Captain Jack Sparrow from the database now
    pirate_parrots: list[PirateParrot] = pirate_parrot_dao.get_all_pirate_parrots()

    for index, pirate_parrot in enumerate(pirate_parrots):
        print(f"parrot: {index}")
        print(f"pirate_parrot.name: {pirate_parrot.name}")
        print(f"pirate_parrot.weapon: {pirate_parrot.weapon}")
