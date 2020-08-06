"""
Mostly constants related to consensus, or p2p connection that are not suitable to be in config
"""

# blocks bearing a timestamp that is slightly larger than current epoch will be broadcasted
ALLOWED_FUTURE_BLOCKS_TIME_BROADCAST = 15

# blocks bearing a timestamp that is slightly larger than current epoch will be considered valid
ALLOWED_FUTURE_BLOCKS_TIME_VALIDATION = 15

# Current minor block size is up to 6M gas / 4 (zero-byte gas) = 1.5M
# Per-command size is now 128M so 128M / 1.5M = 85
MINOR_BLOCK_BATCH_SIZE = 50

MINOR_BLOCK_HEADER_LIST_LIMIT = 100

# max number of transactions from NEW_TRANSACTION_LIST command
NEW_TRANSACTION_LIST_LIMIT = 1000

ROOT_BLOCK_BATCH_SIZE = 100

ROOT_BLOCK_HEADER_LIST_LIMIT = 500

SYNC_TIMEOUT = 30

BLOCK_UNCOMMITTED = 0  # The other slaves and the master may not have the block info
BLOCK_COMMITTING = 1  # The block info is propagating to other slaves and the master
BLOCK_COMMITTED = 2  # The other slaves and the master have received the block info

ROOT_CHAIN_POSW_CONTRACT_BYTECODE = bytes.fromhex(
    """
608060405234801561001057600080fd5b50610700806100206000396000f3fe60806040526004361061007b5760003560e01c8063853828b61161004e578063853828b6146101b5578063a69df4b5146101ca578063f83d08ba146101df578063fd8c4646146101e75761007b565b806316934fc4146100d85780632e1a7d4d1461013c578063485d3834146101685780636c19e7831461018f575b336000908152602081905260409020805460ff16156100cb5760405162461bcd60e51b815260040180806020018281038252602681526020018061062e6026913960400191505060405180910390fd5b6100d5813461023b565b50005b3480156100e457600080fd5b5061010b600480360360208110156100fb57600080fd5b50356001600160a01b031661029b565b6040805194151585526020850193909352838301919091526001600160a01b03166060830152519081900360800190f35b34801561014857600080fd5b506101666004803603602081101561015f57600080fd5b50356102cf565b005b34801561017457600080fd5b5061017d61034a565b60408051918252519081900360200190f35b610166600480360360208110156101a557600080fd5b50356001600160a01b0316610351565b3480156101c157600080fd5b506101666103c8565b3480156101d657600080fd5b50610166610436565b6101666104f7565b3480156101f357600080fd5b5061021a6004803603602081101561020a57600080fd5b50356001600160a01b0316610558565b604080519283526001600160a01b0390911660208301528051918290030190f35b8015610297576002820154808201908111610291576040805162461bcd60e51b81526020600482015260116024820152706164646974696f6e206f766572666c6f7760781b604482015290519081900360640190fd5b60028301555b5050565b600060208190529081526040902080546001820154600283015460039093015460ff9092169290916001600160a01b031684565b336000908152602081905260409020805460ff1680156102f3575080600101544210155b6102fc57600080fd5b806002015482111561030d57600080fd5b6002810180548390039055604051339083156108fc029084906000818181858888f19350505050158015610345573d6000803e3d6000fd5b505050565b6203f48081565b336000908152602081905260409020805460ff16156103a15760405162461bcd60e51b81526004018080602001828103825260268152602001806106546026913960400191505060405180910390fd5b6003810180546001600160a01b0319166001600160a01b038416179055610297813461023b565b6103d06105fa565b5033600090815260208181526040918290208251608081018452815460ff16151581526001820154928101929092526002810154928201839052600301546001600160a01b031660608201529061042657600080fd5b61043381604001516102cf565b50565b336000908152602081905260409020805460ff16156104865760405162461bcd60e51b815260040180806020018281038252602b8152602001806106a1602b913960400191505060405180910390fd5b60008160020154116104df576040805162461bcd60e51b815260206004820152601b60248201527f73686f756c642068617665206578697374696e67207374616b65730000000000604482015290519081900360640190fd5b805460ff191660019081178255426203f48001910155565b336000908152602081905260409020805460ff166105465760405162461bcd60e51b815260040180806020018281038252602781526020018061067a6027913960400191505060405180910390fd5b805460ff19168155610433813461023b565b6000806105636105fa565b506001600160a01b03808416600090815260208181526040918290208251608081018452815460ff161580158252600183015493820193909352600282015493810193909352600301549092166060820152906105c75750600091508190506105f5565b60608101516000906001600160a01b03166105e35750836105ea565b5060608101515b604090910151925090505b915091565b6040518060800160405280600015158152602001600081526020016000815260200160006001600160a01b03168152509056fe73686f756c64206f6e6c7920616464207374616b657320696e206c6f636b656420737461746573686f756c64206f6e6c7920736574207369676e657220696e206c6f636b656420737461746573686f756c64206e6f74206c6f636b20616c72656164792d6c6f636b6564206163636f756e747373686f756c64206e6f7420756e6c6f636b20616c72656164792d756e6c6f636b6564206163636f756e7473a265627a7a72315820f2c044ad50ee08e7e49c575b49e8de27cac8322afdb97780b779aa1af44e40d364736f6c634300050b0032
""".strip()
)

# The following code is compiled with:
#    solc (0.5.17+commit.d19bba13.Linux.g++) --bin --optimize --optimize-runs 200 --evm-version petersburg
# Source code commit 7a762f5e.
NON_RESERVED_NATIVE_TOKEN_CONTRACT_BYTECODE = bytes.fromhex(
    """
60e0604052603c6080819052600160a052606460c052600580547001000000000000000000000000000000006001600160801b0319909116909217600160801b600160c01b031916919091176001600160c01b0316786400000000000000000000000000000000000000000000000017905534801561007d57600080fd5b50604051611be1380380611be1833981810160405260208110156100a057600080fd5b5051600080546001600160a01b039092166001600160a01b03199283168117825560098054909316179091556001805460ff191681178155618bb090915260066020527f2ba564dfea427dab268994f8b62c33f976f4d73ab297e6772a26c96a94aec8008054600160401b600160e01b03196001600160401b03199091169092179190911668010000000000000000179055611aa0806101416000396000f3fe6080604052600436106101355760003560e01c806356e4b68b116100ab5780639ea41be71161006f5780639ea41be7146104f1578063b187bd2614610524578063b9ae736414610539578063bc1fc2091461054e578063eb06bc8214610581578063fe67a54b146105b457610135565b806356e4b68b146103c45780635cebc168146103d95780635fc81df11461040c5780636aecd9d71461046f5780638556fed2146104af57610135565b806332353fbd116100fd57806332353fbd1461028c5780633c69e3d2146102a15780633ccfd60b146102e657806344637c8d146102fb5780635254298a14610336578063568f02f81461037d57610135565b806308bfc3001461013a5780630f2dc31a1461019b5780631c05ca8d146101d657806321ce16031461020757806327e235e314610247575b600080fd5b34801561014657600080fd5b5061014f6105c9565b604080516001600160801b03968716815294861660208601526001600160a01b03909316848401526001600160401b039091166060840152909216608082015290519081900360a00190f35b3480156101a757600080fd5b506101d4600480360360408110156101be57600080fd5b506001600160801b03813516906020013561060a565b005b3480156101e257600080fd5b506101eb610774565b604080516001600160a01b039092168252519081900360200190f35b6101d46004803603606081101561021d57600080fd5b5080356001600160801b0390811691602081013590911690604001356001600160401b0316610783565b34801561025357600080fd5b5061027a6004803603602081101561026a57600080fd5b50356001600160a01b03166107ff565b60408051918252519081900360200190f35b34801561029857600080fd5b506101d4610811565b3480156102ad57600080fd5b506101d4600480360360608110156102c457600080fd5b506001600160401b03813581169160208101358216916040909101351661087f565b3480156102f257600080fd5b506101d46109b6565b34801561030757600080fd5b506101d46004803603604081101561031e57600080fd5b506001600160801b0381351690602001351515610a8b565b34801561034257600080fd5b506103696004803603602081101561035957600080fd5b50356001600160801b0316610b03565b604080519115158252519081900360200190f35b34801561038957600080fd5b50610392610b18565b604080516001600160801b0390941684526001600160401b039283166020850152911682820152519081900360600190f35b3480156103d057600080fd5b506101eb610b43565b3480156103e557600080fd5b506101d4600480360360208110156103fc57600080fd5b50356001600160a01b0316610b52565b34801561041857600080fd5b5061043f6004803603602081101561042f57600080fd5b50356001600160801b0316610bc1565b604080516001600160401b0390941684526001600160a01b03909216602084015282820152519081900360600190f35b6101d46004803603606081101561048557600080fd5b5080356001600160801b0390811691602081013590911690604001356001600160401b0316610bf6565b3480156104bb57600080fd5b506101d4600480360360408110156104d257600080fd5b5080356001600160801b031690602001356001600160a01b0316610c03565b3480156104fd57600080fd5b5061043f6004803603602081101561051457600080fd5b50356001600160801b0316610cac565b34801561053057600080fd5b50610369610cea565b34801561054557600080fd5b506101d4610cf3565b34801561055a57600080fd5b506101d46004803603602081101561057157600080fd5b50356001600160a01b0316610d4e565b34801561058d57600080fd5b506101d4600480360360208110156105a457600080fd5b50356001600160801b0316610dbd565b3480156105c057600080fd5b506101d4610f13565b6003546004546001546002546001600160801b0380851694600160801b90048116936001600160a01b03169263ffffffff6101009091041691169091929394565b6001600160801b038216600090815260066020526040902080546001600160401b031661067e576040805162461bcd60e51b815260206004820152601760248201527f546f6b656e20494420646f65736e27742065786973742e000000000000000000604482015290519081900360640190fd5b8054600160401b90046001600160a01b031633146106cd5760405162461bcd60e51b81526004018080602001828103825260228152602001806118ca6022913960400191505060405180910390fd5b600181018054830190819055821115610722576040805162461bcd60e51b815260206004820152601260248201527120b23234ba34b7b71037bb32b9333637bb9760711b604482015290519081900360640190fd5b61072a61179a565b8154600160401b90046001600160a01b031681526001600160801b0384166020820152604081018390526000806060838264514b430004600019f161076e57600080fd5b50505050565b6009546001600160a01b031681565b6009546001600160a01b03163314806107a557506009546001600160a01b0316155b6107ed576040805162461bcd60e51b8152602060048201526014602482015273082c6c6cad8cae4c2e8dee440dad2e6dac2e8c6d60631b604482015290519081900360640190fd5b6107fa838383600161110b565b505050565b60076020526000908152604090205481565b6000546001600160a01b0316331461085e576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b610866611630565b1561087357610873611669565b6001805460ff19169055565b6000546001600160a01b031633146108cc576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b600154600160281b90046001600160801b03161561091b5760405162461bcd60e51b81526004018080602001828103825260368152602001806118316036913960400191505060405180910390fd5b603c6001600160401b038216116109635760405162461bcd60e51b81526004018080602001828103825260298152602001806119ff6029913960400191505060405180910390fd5b600580546001600160801b03196001600160401b03948516600160801b0267ffffffffffffffff60801b19968616600160c01b026001600160c01b03909316929092179590951617939093169116179055565b6004546001600160a01b0316331415610a005760405162461bcd60e51b8152600401808060200182810382526044815260200180611a286044913960600191505060405180910390fd5b3360009081526007602052604090205480610a4c5760405162461bcd60e51b81526004018080602001828103825260218152602001806119876021913960400191505060405180910390fd5b336000818152600760205260408082208290555183156108fc0291849190818181858888f19350505050158015610a87573d6000803e3d6000fd5b5050565b6000546001600160a01b03163314610ad8576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b6001600160801b03919091166000908152600860205260409020805460ff1916911515919091179055565b60086020526000908152604090205460ff1681565b6005546001600160801b038116906001600160401b03600160801b8204811691600160c01b90041683565b6000546001600160a01b031681565b6000546001600160a01b03163314610b9f576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b600980546001600160a01b0319166001600160a01b0392909216919091179055565b600660205260009081526040902080546001909101546001600160401b03821691600160401b90046001600160a01b03169083565b6107fa838383600061110b565b6001600160801b038216600090815260066020526040902054600160401b90046001600160a01b03163314610c695760405162461bcd60e51b815260040180806020018281038252602681526020018061180b6026913960400191505060405180910390fd5b6001600160801b03909116600090815260066020526040902080546001600160a01b03909216600160401b02600160401b600160e01b0319909216919091179055565b6001600160801b0316600090815260066020526040902080546001909101546001600160401b03821692600160401b9092046001600160a01b031691565b60015460ff1690565b6000546001600160a01b03163314610d40576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b6001805460ff191681179055565b6000546001600160a01b03163314610d9b576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b600080546001600160a01b0319166001600160a01b0392909216919091179055565b6000546001600160a01b03163314610e0a576040805162461bcd60e51b815260206004820152601b60248201526000805160206118aa833981519152604482015290519081900360640190fd5b6001600160801b0381166000908152600660205260409020546001600160401b031615610e685760405162461bcd60e51b81526004018080602001828103825260258152602001806119a86025913960400191505060405180910390fd5b6003546001600160801b0382811691161415610ecb576040805162461bcd60e51b815260206004820152601960248201527f546f6b656e2063616e277420626520696e2061637574696f6e00000000000000604482015290519081900360640190fd5b6001600160801b031660009081526006602052604090208054600160401b67ffffffffffffffff19909116426001600160401b031617600160401b600160e01b031916179055565b60015460ff1615610f60576040805162461bcd60e51b815260206004820152601260248201527120bab1ba34b7b71034b9903830bab9b2b21760711b604482015290519081900360640190fd5b610f68611630565b610fb2576040805162461bcd60e51b815260206004820152601660248201527520bab1ba34b7b7103430b9903737ba1032b73232b21760511b604482015290519081900360640190fd5b6003546004546001600160a01b0316600090815260076020526040902054600160801b9091046001600160801b03161115610fe957fe5b600380546004546001600160a01b031660009081526007602052604080822080546001600160801b03600160801b95869004811690910390915593549051919392900490911680156108fc029183818181858288f19350505050158015611054573d6000803e3d6000fd5b5060048054600380546001600160801b0390811660009081526006602090815260408083208054600160401b600160e01b0319166001600160a01b03978816600160401b0217905584548416835291829020805467ffffffffffffffff1916426001600160401b031617905594549254815193909416835292169281019290925280517f64bb607a8887443bda664340203d98f768ced2874cab4af7c0f6d913aabcf1559281900390910190a1611109611669565b565b60015460ff1615611158576040805162461bcd60e51b815260206004820152601260248201527120bab1ba34b7b71034b9903830bab9b2b21760711b604482015290519081900360640190fd5b611160611630565b156111875761116d610f13565b600154600160281b90046001600160801b03161561118757fe5b600154600160281b90046001600160801b031661122a576001805465010000000000600160a81b031916600160281b426001600160801b038181169290920292909217909255600554600280546001600160801b031916918416909201909216919091179055801561122a5760405162461bcd60e51b81526004018080602001828103825260328152602001806117d96032913960400191505060405180910390fd5b611233846116c7565b6001600160801b0384166000908152600660205260409020546001600160401b0316156112a7576040805162461bcd60e51b815260206004820152601760248201527f546f6b656e20496420616c726561647920657869737473000000000000000000604482015290519081900360640190fd5b600154610100900463ffffffff166001600160401b038316146112fb5760405162461bcd60e51b81526004018080602001828103825260318152602001806118ec6031913960400191505060405180910390fd5b600554600160c01b90046001600160401b0316670de0b6b3a7640000026001600160801b038416101561135f5760405162461bcd60e51b81526004018080602001828103825260328152602001806119cd6032913960400191505060405180910390fd5b60055460035460646001600160801b03600160801b9283900481166001600160401b0393909404929092168302821604909101811690841610156113d45760405162461bcd60e51b81526004018080602001828103825260438152602001806118676043913960600191505060405180910390fd5b8015611434576003546001600160801b03600160801b9091048116600202811690841610156114345760405162461bcd60e51b815260040180806020018281038252603b81526020018061194c603b913960400191505060405180910390fd5b3361143d6117b8565b50604080516060810182526001600160801b03808816825286166020808301919091526001600160a01b03841682840181905260009081526007909152919091205434908101908110156114cd576040805162461bcd60e51b815260206004820152601260248201527120b23234ba34b7b71037bb32b9333637bb9760711b604482015290519081900360640190fd5b6001600160a01b03831660009081526007602090815260409091208290558201516001600160801b031681101561154b576040805162461bcd60e51b815260206004820152601a60248201527f4e6f7420656e6f7567682062616c616e636520746f206269642e000000000000604482015290519081900360640190fd5b81516003805460208501516001600160801b03199091166001600160801b03938416178316600160801b918416919091021790556040830151600480546001600160a01b0319166001600160a01b039092169190911790556002544282169116116115b257fe5b83156115e45760028054426001600160801b038083169182038116849004909103166001600160801b03199091161790555b600254426001600160801b039182160390603c908216101561162657600280546001600160801b03808216603c85900301166001600160801b03199091161790555b5050505050505050565b6002546000906001600160801b0390811642909116108015906116645750600154600160281b90046001600160801b031615155b905090565b6000600355600480546001600160a01b031916905560018054600280546001600160801b031916905563ffffffff61010065010000000000600160a81b031983168190048216840190911602610100600160a81b0319909116179055565b6001600160801b03811660009081526008602052604090205460ff1661173157621a5c73816001600160801b0316116117315760405162461bcd60e51b815260040180806020018281038252602f81526020018061191d602f913960400191505060405180910390fd5b6743a3163a81075073816001600160801b03161115611797576040805162461bcd60e51b815260206004820152601960248201527f546f6b656e2049442063616e277420657863656564206d617800000000000000604482015290519081900360640190fd5b50565b60405180606001604052806003906020820280388339509192915050565b60408051606081018252600080825260208201819052918101919091529056fe46697273742061756374696f6e206f662061206e657720726f756e642063616e6e6f7420626520616363656c6572617465644f6e6c7920746865206f776e65722063616e207472616e73666572206f776e6572736869702e41756374696f6e2073657474696e672063616e6e6f74206265206d6f646966696564207768656e206974206973206f6e676f696e672e4269642070726963652073686f756c64206265206c6172676572207468616e2063757272656e74206869676865737420626964207769746820696e6372656d656e742e4f6e6c792073757065727669736f7220697320616c6c6f7765642e00000000004f6e6c7920746865206f776e65722063616e206d696e74206e657720746f6b656e2e54617267657420726f756e64206f662061756374696f6e2068617320656e646564206f72206e6f7420737461727465642e546865206c656e677468206f6620746f6b656e206e616d65204d555354206265206c6172676572207468616e20342e426964207072696365206d7573742062652067726561746572207468616e203278206f662063757272656e742061756374696f6e2070726963652e4e6f2062616c616e636520617661696c61626c6520746f2077697468647261772e546f6b656e2073686f756c64206e6f742068617665206265656e2061756374696f6e65642e4269642070726963652073686f756c64206265206c6172676572207468616e206d696e696d756d206269642070726963652e4475726174696f6e2073686f756c64206265206c6f6e676572207468616e2035206d696e757465732e48696768657374206269646465722063616e6e6f742077697468647261772062616c616e63652074696c6c2074686520656e64206f6620746869732061756374696f6e2ea265627a7a723158203040309df9b46cb61b40bf058d3b2123e6cf52148186608a97e43d7331cd13f864736f6c63430005110032000000000000000000000000a92885095A33E45A3C018Df7Aa6242B62Acb9718
""".strip()
)

GENERAL_NATIVE_TOKEN_CONTRACT_BYTECODE = bytes.fromhex(
    """
60806040526003805478056bc75e2d63100000000000000000000000000000000000006001600160801b0319909116678ac7230489e80000176001600160801b03161790556008805460ff1916905534801561005a57600080fd5b5060405161192c38038061192c8339818101604052604081101561007d57600080fd5b508051602090910151600180546001600160a01b0319166001600160a01b038085169190911790915581166100c357600080546001600160a01b031916301790556100df565b600080546001600160a01b0319166001600160a01b0383161790555b50506004805460ff1916600117905561182f806100fd6000396000f3fe6080604052600436106101355760003560e01c806382e1521d116100ab578063bf03314a1161006f578063bf03314a146104db578063bffa8bd0146104e3578063ce9e8c4714610514578063ceca031814610581578063dc68f0a0146105a7578063f9c94eb7146105bc57610135565b806382e1521d146103925780639447e58c146103c55780639ed2c7ef1461043a578063bb9288541461046d578063bc1fc209146104a857610135565b80635ae8f7f1116100fd5780635ae8f7f11461023f5780636d27af8c146102a8578063735e0e19146102ed578063764a27ef146103255780637e081270146103515780637e932d321461036657610135565b8063041e6c091461013a578063054f7d9c1461016357806313dee2151461017857806321a2b36e146101cc57806356e4b68b1461020e575b600080fd5b34801561014657600080fd5b5061014f6105ef565b604080519115158252519081900360200190f35b34801561016f57600080fd5b5061014f6105f8565b34801561018457600080fd5b506101ba6004803603604081101561019b57600080fd5b5080356001600160801b031690602001356001600160a01b0316610601565b60408051918252519081900360200190f35b3480156101d857600080fd5b506101ba600480360360408110156101ef57600080fd5b5080356001600160801b031690602001356001600160a01b031661061e565b34801561021a57600080fd5b5061022361063b565b604080516001600160a01b039092168252519081900360200190f35b34801561024b57600080fd5b506102846004803603606081101561026257600080fd5b506001600160801b03813581169160208101358216916040909101351661064a565b6040805167ffffffffffffffff909316835260208301919091528051918290030190f35b3480156102b457600080fd5b506102eb600480360360408110156102cb57600080fd5b5080356001600160801b0316906020013567ffffffffffffffff166108b7565b005b6102eb6004803603606081101561030357600080fd5b506001600160801b0381358116916020810135821691604090910135166109d2565b34801561033157600080fd5b506102eb6004803603602081101561034857600080fd5b50351515610e3c565b34801561035d57600080fd5b50610223610e9c565b34801561037257600080fd5b506102eb6004803603602081101561038957600080fd5b50351515610eab565b34801561039e57600080fd5b5061014f600480360360208110156103b557600080fd5b50356001600160801b0316610f0b565b3480156103d157600080fd5b506103f8600480360360208110156103e857600080fd5b50356001600160801b0316610f20565b604080516001600160a01b03909516855267ffffffffffffffff90931660208501526001600160801b0391821684840152166060830152519081900360800190f35b34801561044657600080fd5b506102eb6004803603602081101561045d57600080fd5b50356001600160801b0316610f6a565b34801561047957600080fd5b506102eb6004803603604081101561049057600080fd5b506001600160801b03813581169160200135166110a2565b3480156104b457600080fd5b506102eb600480360360208110156104cb57600080fd5b50356001600160a01b031661111f565b6102eb61118e565b3480156104ef57600080fd5b506104f86112a4565b604080516001600160801b039092168252519081900360200190f35b34801561052057600080fd5b5061054f6004803603604081101561053757600080fd5b506001600160801b03813581169160200135166112b3565b6040805167ffffffffffffffff909416845260208401929092526001600160a01b031682820152519081900360600190f35b6102eb6004803603602081101561059757600080fd5b50356001600160801b0316611401565b3480156105b357600080fd5b506104f861151a565b3480156105c857600080fd5b506102eb600480360360208110156105df57600080fd5b50356001600160801b0316611530565b60045460ff1681565b60085460ff1681565b600560209081526000928352604080842090915290825290205481565b600660209081526000928352604080842090915290825290205481565b6001546001600160a01b031681565b600854600090819060ff161561069a576040805162461bcd60e51b815260206004820152601060248201526f21b7b73a3930b1ba10333937bd32b71760811b604482015290519081900360640190fd5b6000546001600160a01b031633146106e35760405162461bcd60e51b81526004018080602001828103825260258152602001806116da6025913960400191505060405180910390fd5b60008060006106f288876112b3565b919450925090506001600160801b03878116908716810290808402908490828161071857fe5b041461076b576040805162461bcd60e51b815260206004820152601760248201527f41766f69642075696e74323536206f766572666c6f772e000000000000000000604482015290519081900360640190fd5b6001600160801b038a1660009081526005602090815260408083206001600160a01b03871684529091529020548111156107d65760405162461bcd60e51b81526004018080602001828103825260238152602001806117726023913960400191505060405180910390fd5b6001600160801b038a1660009081526006602090815260408083206001600160a01b03871684529091529020548281019081101561085b576040805162461bcd60e51b815260206004820152601860248201527f41766f6964206164646974696f6e206f766572666c6f772e0000000000000000604482015290519081900360640190fd5b6001600160801b038b1660008181526005602090815260408083206001600160a01b0390981680845297825280832080549690960390955591815260068252838120958152949052922091909155509092509050935093915050565b6001600160801b0382166000908152600260205260409020546001600160a01b0316331461092c576040805162461bcd60e51b815260206004820152601f60248201527f4f6e6c792061646d696e2063616e2073657420726566756e6420726174652e00604482015290519081900360640190fd5b8067ffffffffffffffff16600a11158015610952575060648167ffffffffffffffff1611155b61098d5760405162461bcd60e51b815260040180806020018281038252602f8152602001806117cc602f913960400191505060405180910390fd5b6001600160801b039091166000908152600260205260409020805467ffffffffffffffff909216600160a01b0267ffffffffffffffff60a01b19909216919091179055565b60085460ff1615610a1d576040805162461bcd60e51b815260206004820152601060248201526f21b7b73a3930b1ba10333937bd32b71760811b604482015290519081900360640190fd5b60045460ff1615610a95576001600160801b03831660009081526007602052604090205460ff16610a95576040805162461bcd60e51b815260206004820152601860248201527f546f6b656e20494420646f6573206e6f742065786973742e0000000000000000604482015290519081900360640190fd5b6743a3163a81075073836001600160801b03161115610af3576040805162461bcd60e51b815260206004820152601560248201527426b0bc103a37b5b2b71024a2103932b0b1b432b21760591b604482015290519081900360640190fd5b826001600160801b0316618bb01415610b4c576040805162461bcd60e51b815260206004820152601660248201527521b0b713ba103132903232b330bab63a103a37b5b2b760511b604482015290519081900360640190fd5b816001600160801b0316600010610ba6576040805162461bcd60e51b81526020600482015260196024820152782b30b63ab29039b437bab632103132903737b716bd32b9379760391b604482015290519081900360640190fd5b806001600160801b0316600010610c00576040805162461bcd60e51b81526020600482015260196024820152782b30b63ab29039b437bab632103132903737b716bd32b9379760391b604482015290519081900360640190fd5b6003546001600160801b03908116818316026152089184169190910210610c585760405162461bcd60e51b81526004018080602001828103825260378152602001806117956037913960400191505060405180910390fd5b6003546001600160801b038481166000908152600560209081526040808320338452909152902054600160801b90920416349091011015610cca5760405162461bcd60e51b81526004018080602001828103825260308152602001806117426030913960400191505060405180910390fd5b6001600160801b0380841660009081526002602090815260408083206005835281842060035482546001600160a01b031686529381905291909320549293909291161180610d3757506001820154610d37906001600160801b0380821691600160801b90041686866115d7565b610d725760405162461bcd60e51b81526004018080602001828103825260238152602001806116946023913960400191505060405180910390fd5b336000908152602082905260409020543490810190811015610dd0576040805162461bcd60e51b815260206004820152601260248201527120b23234ba34b7b71037bb32b9333637bb9760711b604482015290519081900360640190fd5b33600081815260209390935260409092205581546001830180546001600160801b0319166001600160801b03968716178616600160801b9590961694909402949094179092556001600160a01b03199092161767ffffffffffffffff60a01b1916601960a11b17905550565b6001546001600160a01b03163314610e89576040805162461bcd60e51b815260206004820152601b60248201526000805160206116ff833981519152604482015290519081900360640190fd5b6004805460ff1916911515919091179055565b6000546001600160a01b031681565b6001546001600160a01b03163314610ef8576040805162461bcd60e51b815260206004820152601b60248201526000805160206116ff833981519152604482015290519081900360640190fd5b6008805460ff1916911515919091179055565b60076020526000908152604090205460ff1681565b600260205260009081526040902080546001909101546001600160a01b03821691600160a01b900467ffffffffffffffff16906001600160801b0380821691600160801b90041684565b60085460ff1680610f9c57506001600160801b0381166000908152600260205260409020546001600160a01b03163314155b610fd75760405162461bcd60e51b815260040180806020018281038252602381526020018061171f6023913960400191505060405180910390fd5b6001600160801b03811660009081526005602090815260408083203384529091529020548061104d576040805162461bcd60e51b815260206004820152601b60248201527f53686f756c642068617665206e6f6e2d7a65726f2076616c75652e0000000000604482015290519081900360640190fd5b6001600160801b038216600090815260056020908152604080832033808552925280832083905551909183156108fc02918491818181858888f1935050505015801561109d573d6000803e3d6000fd5b505050565b6001546001600160a01b031633146110ef576040805162461bcd60e51b815260206004820152601b60248201526000805160206116ff833981519152604482015290519081900360640190fd5b600380546001600160801b03928316600160801b029383166001600160801b031990911617909116919091179055565b6001546001600160a01b0316331461116c576040805162461bcd60e51b815260206004820152601b60248201526000805160206116ff833981519152604482015290519081900360640190fd5b600180546001600160a01b0319166001600160a01b0392909216919091179055565b611196611630565b6020816000808064514b430001600019f16111b057600080fd5b8051618bb06001600160801b03821614156111fc5760405162461bcd60e51b81526004018080602001828103825260238152602001806116b76023913960400191505060405180910390fd5b6001600160801b03811660009081526007602052604090205460ff161561126a576040805162461bcd60e51b815260206004820152601960248201527f546f6b656e20616c726561647920726567697374657265642e00000000000000604482015290519081900360640190fd5b6001600160801b03166000908152600760209081526040808320805460ff1916600117905560068252808320338452909152902034905550565b6003546001600160801b031681565b60008060006112c061164e565b506001600160801b03858116600090815260026020908152604091829020825160808101845281546001600160a01b038116808352600160a01b90910467ffffffffffffffff169382019390935260019091015480851693820193909352600160801b909204909216606082015290611371576040805162461bcd60e51b815260206004820152600e60248201526d24b73b30b634b2103a37b5b2b71760911b604482015290519081900360640190fd5b604081015160608201516001600160801b03918216828816029116818161139457fe5b049050600081116113ec576040805162461bcd60e51b815260206004820152601b60248201527f53686f756c642068617665206e6f6e2d7a65726f2076616c75652e0000000000604482015290519081900360640190fd5b60208201519151919450925090509250925092565b6001600160801b0381166000908152600560209081526040808320338452909152902054611476576040805162461bcd60e51b815260206004820152601a60248201527f53686f756c6420626520616e206578697374656420746f6b656e000000000000604482015290519081900360640190fd5b6001600160801b038116600090815260056020908152604080832033845290915290205434908101908110156114f3576040805162461bcd60e51b815260206004820152601960248201527f52657365727665642062616c616e6365206f766572666c6f7700000000000000604482015290519081900360640190fd5b6001600160801b039091166000908152600560209081526040808320338452909152902055565b600354600160801b90046001600160801b031681565b6001600160801b0381166000908152600660209081526040808320338452909152902054806115a6576040805162461bcd60e51b815260206004820152601b60248201527f53686f756c642068617665206e6f6e2d7a65726f2076616c75652e0000000000604482015290519081900360640190fd5b6001600160801b038216600081815260066020908152604080832033808552925282209190915561109d91836115f3565b6001600160801b03918216928216929092029281169116021090565b60006115fd611675565b84815260208082018590526040820184905282606083600064514b430002600019f161162857600080fd5b509392505050565b60405180602001604052806001906020820280388339509192915050565b60408051608081018252600080825260208201819052918101829052606081019190915290565b6040518060600160405280600390602082028038833950919291505056fe496e76616c6964206e65772065786368616e676520726174652070726f706f73616c2e44656661756c7420746f6b656e2063616e6e6f7420626520726567697374657265642e4f6e6c792063616c6c65722063616e20696e766f6b6520746869732066756e6374696f6e2e4f6e6c792073757065727669736f7220697320616c6c6f7765642e00000000004e6f7420616c6c6f77656420666f72206e617469766520746f6b656e2061646d696e2e53686f756c642068617665207265736572766520616d6f756e742067726561746572207468616e206d696e696d756d2e53686f756c64206861766520656e6f75676820726573657276657320746f207061792e52657175697265732065786368616e67652072617465202a203231303030203c206d696e476173526573657276654d61696e7461696e2e526566756e642070657274656e746167652073686f756c64206265206265747765656e20313020616e64203130302ea265627a7a72315820923fb9d8c38c521f16b3886f1bc6ca4175913f9387285f6fbcafb779b40bf55764736f6c63430005110032000000000000000000000000a92885095A33E45A3C018Df7Aa6242B62Acb97180000000000000000000000000000000000000000000000000000000000000000
""".strip()
)

MAINNET_ENABLE_NON_RESERVED_NATIVE_TOKEN_CONTRACT_TIMESTAMP = 1588291200
MAINNET_ENABLE_GENERAL_NATIVE_TOKEN_CONTRACT_TIMESTAMP = 1588291200
MAINNET_ENABLE_POSW_STAKING_DECAY_TIMESTAMP = 1588291200

PRECOMPILED_CONTRACTS_AFTER_EVM_ENABLED = [
    bytes.fromhex("000000000000000000000000000000514b430001"),
    bytes.fromhex("000000000000000000000000000000514b430002"),
    bytes.fromhex("000000000000000000000000000000514b430003"),
]


PRECOMPILED_CONTRACT_MINT_MNT = bytes.fromhex(
    "000000000000000000000000000000514b430004"
)
PRECOMPILED_CONTRACT_QUERY_MNT_BALANCE = bytes.fromhex(
    "000000000000000000000000000000514b430005"
)
