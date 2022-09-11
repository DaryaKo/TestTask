import motor.motor_asyncio

from config import MONGO_DETAILS


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.test_db

employee_collection = database.get_collection("employee")


def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"],
    }