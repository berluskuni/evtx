__author__ = 'berluskuni'

import mmap
import contextlib
import sys

from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view


def event_to_xml(filename):
    with open("C:\Windows\System32\winevt\Logs\{}.evtx" .format(filename), 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as buf:
            fh = FileHeader(buf, 0x0)
            with open("D:\GIT\EVTX\{}.xml" .format(filename), 'w') as fx:
                fx.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>" '\n')
                fx.write("<Events>" '\n')
                count = 5
                for xml, record in evtx_file_xml_view(fh):
                    if count >= 0:
                        fx.write(xml)
                        count -= 1
                    else:
                        break
                fx.write("</Events>" '\n')


def main():
    if len(sys.argv) != 3:
        print "usage: event.py {--evtx} file (evtx --> name logfile windows event)"
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--evtx':
        event_to_xml(filename)
    else:
        print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
    main()
