module Main where

import Data.List
import System.IO
import Network

-- Thrift libraries
import Thrift
import Thrift.Transport.Handle
import Thrift.Protocol
import Thrift.Protocol.Binary
import Thrift.Server

import HaskellThrift.Ping_pong_Client

port :: PortNumber
port = 9900

clientFunc :: HostName -> PortNumber -> IO ()
clientFunc host p = do
  putStrLn "Client go!"
  h <- connectTo host $ PortNumber p
  let proto = BinaryProtocol h
  result <- ping (proto, proto)
  print result
  tClose h

main :: IO ()
main = do
  clientFunc "localhost" port
