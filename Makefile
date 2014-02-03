default:
	thrift --gen py ping-pong.thrift
	mv gen-py/ gen_py/

clean:
	rm -rf gen_py/ gen-py/
