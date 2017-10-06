# bib-sorter
A simple python script that takes a bib file and generated a sorted version (on the citation keyword) of it.


For example:

####### Input file

@article{harman2001search,
  title={Search-based software engineering},
}

@inproceedings{Mao:2016:SMA:2931037.2931054,
 author = {Mao, Ke and Harman, Mark and Jia, Yue},
}

@article{Georges:2008:JPE:1449955.1449794,
 author = {Georges, Andy and Eeckhout, Lieven and Buytaert, Dries},
}


####### Output file

@article{Georges:2008:JPE:1449955.1449794,
 author = {Georges, Andy and Eeckhout, Lieven and Buytaert, Dries},
}

@article{harman2001search,
  title={Search-based software engineering},
}

@inproceedings{Mao:2016:SMA:2931037.2931054,
 author = {Mao, Ke and Harman, Mark and Jia, Yue},
}

