# Script to be called as cibuildwheel before-all

set -e

CIBW_PLATFORM=$(uname)
CIBW_BUILD=$AUDITWHEEL_POLICY

echo D $CIBW_PLATFORM B $CIBW_BUILD

if [[ $CIBW_PLATFORM == "Linux" ]]; then
    echo "platform is Linux."
elif [[ $CIBW_PLATFORM == "Darwin" ]]; then
    echo "platform is macOS."
    echo "GMP: $(find / -name gmp.h)"
    echo "PARI: $(find / -name pari.h)"
    echo "LIBGMP: $(find / -name libgmp.a)"
    echo "LIBPARI: $(find / -name libpari.a)"
    echo "GMPXX: $(find / -name gmpxx.*)"
elif [[ $CIBW_PLATFORM == *"MINGW64_NT"* ]]; then
    echo "platform is Windows."
    echo "GMP: $(find /c/msys64 -name gmp.h)"
    echo "PARI: $(find /d -name pari.h)"
    echo "LIBGMP: $(find /c/msys64 -name libgmp.a)"
    echo "LIBPARI: $(find /d -name libpari.a)"
else
    echo "unknown platform: $CIBW_PLATFORM"
fi
