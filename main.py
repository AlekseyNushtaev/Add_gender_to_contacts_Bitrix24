from bitrix.bitrix import BitrixWorker
from config import WEBHOOK
from database.database import DbWorker
from database.models import Session, NamesMan, NamesWoman


def main():
    session = Session()

    db_worker = DbWorker(session)
    db_worker.names_to_db(NamesMan, "man")
    db_worker.names_to_db(NamesWoman, "woman")

    bitrix_worker = BitrixWorker(WEBHOOK)
    bitrix_worker.add_sex_field()
    contacts = bitrix_worker.get_contacts()

    for contact in contacts:
        sex = db_worker.find_name(contact["NAME"])
        if sex:
            bitrix_worker.update_sex_field(contact["ID"], sex)

    session.close()


if __name__ == "__main__":
    main()
