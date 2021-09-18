import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--num_y', help = 'the number of years', type = int)
parser.add_argument('--num_d', help = 'the number of days', type = int)
args = parser.parse_args()


c_dt = datetime.datetime.today()
dtdelta = datetime.timedelta(days = args.num_d)
f_dt = c_dt + dtdelta

print('Current date: ', c_dt)
if args.num_y:
    print('Given years: ', args.num_y)
else:
    print('Given years: not given')
if args.num_d:
    print('Given days: ', args.num_d)
else:
    print('Given days: not given')
print('Final date: ', f_dt)

