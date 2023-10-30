LATEST="9fd5a29585234b32cdd81cea71d71408760c489b"
ORIGINAL="6322db01226ef4a561244ce90a5df946b163f7ba"

pushd .
cd coolstuff-quarkus

git diff $ORIGINAL $LATEST -- src/main/java/com/redhat/coolstore/service/InventoryNotificationMDB.java

popd

