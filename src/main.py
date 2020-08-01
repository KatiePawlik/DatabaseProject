from models.User import User
from models.Doctor import Doctor
from database.sqlUtils import sqlUtils

print(User().name)
print(Doctor().name)

userGenerator = User()
addUsers = sqlUtils()
addUsers.addRowtoTable(userGenerator.userId, userGenerator.name, userGenerator.password_hash)
