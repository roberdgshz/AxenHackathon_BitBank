--create database BitBankDB;
--use BitBankDB;

create table Accounts(
	AccountID		bigint primary key identity,
	AccountUsername varchar(255) unique not null,
	AccountPassword	varchar(255) not null, --- Hash
	AccountEmail	varchar(255) not null,
	AccountNIP		int not null
);

create table Coins(
	CoinID		bigint primary key identity,
	CoinName	varchar(100) not null, --Bitcoin
	CoinKey		varchar(10) not null, --BTC
	CoinImgPath	varchar(255), -- /images/coins/btc.png
	CoinValue	bigint not null -- El valor de la moneda será referenciado con respecto a BTC. Ejemplo: 1 EURO equiva a 0.0000114 BTC (26/11/2024 5:39 P.M.) 
);

create table Wallet(
	WalletID			bigint primary key identity,
	WalletBalance		bigint not null,
	WalletAccountsID	bigint not null, --FK
	WalletCoinsID		bigint not null, --FK
);

create table WalletCoins(
	WalletCoinID			bigint primary key identity,
	WalletCoinQuantity		bigint not null, 
 	WalletCoinWalletID		bigint not null, --FK
);

create table ProfileAccounts(
	ProfileID			bigint primary key identity,
	ProfileName			varchar(255) not null,
	ProfileLastName		varchar(255) not null,
	PofileNumberPhone	varchar(15),
	ProfileAccountID	bigint --FK
);

create table Transactions(
	TransactionID			bigint primary key identity,
	TransactionAmount		bigint not null,
	TransactionDate			smalldatetime not null,
	TransactionReceiver		bigint not null, --FK 
	TransactionTransmitter	bigint not null  --FK 
);

create table AuditLogs(
	AuditLogID			bigint primary key identity,
	AuditLogAccount		bigint not null, -- FK 
	AuditLogDescription	text not null, --
	AuditLogTime		smalldatetime, --Fecha
);
