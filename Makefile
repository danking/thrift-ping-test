default:
	thrift --gen py ping_pong.thrift
	thrift --gen hs ping_pong.thrift
	mv gen-py/ gen_py/
	mv gen-hs/ HaskellThrift
	pushd HaskellThrift; for f in * ; do sed -e '/class Ping_pong/! s/Ping_pong/HaskellThrift.Ping_pong/' $$f > ___$$f ; mv ___$$f $$f ; done; popd

clean:
	rm -rf gen_py/ gen-py/ HaskellThrift/ gen-hs/
