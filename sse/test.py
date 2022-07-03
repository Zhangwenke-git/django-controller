
from datetime import datetime
if __name__ == "__main__":
    s= "2022-12-01 12:13:11"

    x = datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
    print(x.year,x.hour)

