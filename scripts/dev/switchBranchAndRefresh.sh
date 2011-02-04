 #!/bin/bash
function cdc {
	cd $COMMON_HOME
}
function cdt {
	cd $THREETWELVE_HOME
}
function cdo {
	cd $OUTCOMES_HOME
}
function pullAll {
	echo "====Pulling all projects===="
	if $REFRESH_OUTCOMES ; then
		cdo; git pull;
	fi

	cdc; git pull;

	if $REFRESH_OIB ; then
		cdt; git pull;
	fi
}
function checkoutAll {
	echo "====Switching branches to "$1"===="
        if $REFRESH_OUTCOMES ; then
                cdo; git checkout $1;
        fi

	cdc; git checkout $1;

	if $REFRESH_OIB ; then
		cdt; git checkout $1;
	fi
}
function deployAll {
	echo "====Deploying all projects===="
	if $REFRESH_OUTCOMES ; then
		cdo; ant clean-deploy;
        fi

	if $REFRESH_OIB ; then
		cdt; ant clean-deploy;
	fi
}
function refreshAllDBs {
	echo "====Refreshing DB for all projects===="
        if $REFRESH_OUTCOMES ; then
		cdo;
		ant load-fixtures;
        fi

	if $REFRESH_OIB ; then
		cdt;
		./refresh_dev_db.sh;
	fi
}

# Make sure whole script fails on error
# Feel free to turn it off if you want to ignore errors
set -e

if [ -z "$1" ]; then 
	echo "Please provide branchName and make sure you have already created the branch"
	echo "usage: $0 [branchName]"
	exit
fi

REFRESH_OUTCOMES=true;
REFRESH_OIB=true;
branchName=$1;
checkoutAll $branchName;
pullAll;
deployAll;
refreshAllDBs;
