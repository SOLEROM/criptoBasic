# bitcoind

*  Bitcoin client, also known as bitcoind on Linux


## deps

* deps: doc/build-unix.md

```
    sudo apt-get install build-essential libtool autotools-dev automake pkg-config bsdmainutils python3
    sudo apt-get install libevent-dev libboost-dev libboost-system-dev libboost-filesystem-dev libboost-test-dev

    //Berkeley DB 4.8
    ./contrib/install_db4.sh `pwd`      //from the root of the repository.


    sudo apt install libsqlite3-dev

    sudo apt install libminiupnpc-dev libnatpmp-dev

    sudo apt-get install libzmq3-dev

    sudo apt install systemtap-sdt-dev

    //Qt 5
    sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools
    sudo apt install qtwayland5

    sudo apt-get install libqrencode-dev

```



##

```
./autogen.sh


libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
libtoolize: copying file 'build-aux/ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
libtoolize: copying file 'build-aux/m4/libtool.m4'
libtoolize: copying file 'build-aux/m4/ltoptions.m4'
libtoolize: copying file 'build-aux/m4/ltsugar.m4'
libtoolize: copying file 'build-aux/m4/ltversion.m4'
libtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:45: installing 'build-aux/compile'
configure.ac:45: installing 'build-aux/config.guess'
configure.ac:45: installing 'build-aux/config.sub'
configure.ac:28: installing 'build-aux/install-sh'
configure.ac:28: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
parallel-tests: installing 'build-aux/test-driver'
libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
libtoolize: copying file 'build-aux/ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
libtoolize: copying file 'build-aux/m4/libtool.m4'
libtoolize: copying file 'build-aux/m4/ltoptions.m4'
libtoolize: copying file 'build-aux/m4/ltsugar.m4'
libtoolize: copying file 'build-aux/m4/ltversion.m4'
libtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:15: installing 'build-aux/compile'
configure.ac:5: installing 'build-aux/config.guess'
configure.ac:5: installing 'build-aux/config.sub'
configure.ac:9: installing 'build-aux/install-sh'
configure.ac:9: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
parallel-tests: installing 'build-aux/test-driver'
libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
libtoolize: copying file 'build-aux/ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'build-aux/m4'.
libtoolize: copying file 'build-aux/m4/libtool.m4'
libtoolize: copying file 'build-aux/m4/ltoptions.m4'
libtoolize: copying file 'build-aux/m4/ltsugar.m4'
libtoolize: copying file 'build-aux/m4/ltversion.m4'
libtoolize: copying file 'build-aux/m4/lt~obsolete.m4'
configure.ac:94: installing 'build-aux/compile'
configure.ac:38: installing 'build-aux/config.guess'
configure.ac:38: installing 'build-aux/config.sub'
configure.ac:48: installing 'build-aux/install-sh'
configure.ac:48: installing 'build-aux/missing'
src/Makefile.am: installing 'build-aux/depcomp'
parallel-tests: installing 'build-aux/test-driver'



```



## ./configure


```
export BDB_PREFIX='/data/redef/bitCoinGit/bitcoin/db4'
./configure BDB_LIBS="-L${BDB_PREFIX}/lib -ldb_cxx-4.8" BDB_CFLAGS="-I${BDB_PREFIX}/include"


```


## make

```
make

make check && sudo make install

```

## elfs

```

bitcoin
bitcoin-cli     bitcoind        bitcoin-qt      bitcoin-tx      bitcoin-util    bitcoin-wallet

```




