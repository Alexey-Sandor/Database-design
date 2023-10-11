from database import BaseModel, engine
from models import *



def main():
    BaseModel.metadata.create_all(engine)


if __name__ == "__main__":
    main()