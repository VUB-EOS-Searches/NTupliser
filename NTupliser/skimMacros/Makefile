# Adding in a few variables to change up flags etc
CC = g++
CFLAGS = -march=native -mtune=native -pthread -fPIC -O2 \
		$(shell root-config --auxcflags) \
		-Wall \
		-Wextra \
		-Wcast-align \
		-Wcast-qual \
		-Wctor-dtor-privacy \
		-Wformat=2 \
		-Winit-self \
		-Winline \
		-Wlogical-op \
		-Wmissing-include-dirs \
		-Wnoexcept \
		-Wold-style-cast \
		-Woverloaded-virtual \
		-Wredundant-decls \
		-Wshadow \
		-Wstrict-null-sentinel \
		-Wswitch-default \
		-Wuseless-cast \
		-Wnon-virtual-dtor \
		-Wzero-as-null-pointer-constant
INCDIR = -isystem$(shell root-config --incdir) \
		 -isystem/usr/include/boost148
LIBS = $(shell root-config --libs) -rdynamic \
	   -L/usr/lib64/boost148 \
	   -lboost_system-mt \
	   -lboost_filesystem-mt \
	   -lboost_program_options \


default: build

clean: _cleanall
_cleanall:
	rm -rf *.o
	rm -rf *.exe

all: _all
build: _all
buildall: _all
_all: skims.exe backup_skims.exe eventCounter.exe printGenInfo.exe

skims.exe: makeDatasetSkim.o AnalysisEvent.o
	$(CC) $(CFLAGS) $(INCDIR) -o skims.exe makeDatasetSkim.o AnalysisEvent.o $(LIBS)

backup_skims.exe: makeDatasetSkimBackup.o AnalysisEvent.o
	$(CC) $(CFLAGS) $(INCDIR) -o backup_skims.exe makeDatasetSkimBackup.o AnalysisEvent.o $(LIBS)

eventCounter.exe: eventCounter.o
	$(CC) $(CFLAGS) $(INCDIR) -o eventCounter.exe eventCounter.o $(LIBS)

printGenInfo.exe: genInfoDebug.o GenInfoEvent.o
	$(CC) $(CFLAGS) $(INCDIR) -o printGenInfo.exe genInfoDebug.o GenInfoEvent.o $(LIBS)

makeDatasetSkim.o: makeDatasetSkim.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c makeDatasetSkim.cpp $(LIBS)

makeDatasetSkimBackup.o: makeDatasetSkimBackup.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c makeDatasetSkimBackup.cpp $(LIBS)

eventCounter.o: eventCounter.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c eventCounter.cpp $(LIBS)

genInfoDebug.o : genInfoDebug.cpp
	$(CC) $(CFLAGS) $(INCDIR) -c genInfoDebug.cpp $(LIBS)

AnalysisEvent.o: AnalysisEvent.C AnalysisEvent.h
	$(CC) $(CFLAGS) $(INCDIR) -c AnalysisEvent.C $(LIBS)

GenInfoEvent.o: GenInfoEvent.C GenInfoEvent.h
	$(CC) $(CFLAGS) $(INCDIR) -c GenInfoEvent.C $(LIBS)

