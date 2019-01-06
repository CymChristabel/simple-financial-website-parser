import sys
import datetime
import xlsxwriter

from securities import Securities


def time_validation(start_time, end_time):
        try:
            start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
            end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        finally:
            return end_time >= start_time

if __name__ == "__main__":
    # Read argument values
    assert len(sys.argv) == 5, 'incorrect number of parameters'

    start_time, end_time, output_filename, search_target = tuple(sys.argv[1:])

    assert search_target in ['0', '1'], 'search target should be 0(Securities) or 1(fund)'
    assert time_validation(start_time, end_time), 'Start time should be less or equal to end time'

    # If filename does not end with .xlsx
    if output_filename.endswith('.xlsx') is False:
        output_filename = output_filename + '.xlsx'

    if search_target == '0':
        Securities(start_time, end_time).post()
    else:
        pass

    # 
    workbook = xlsxwriter.Workbook(filename=output_filename)

