create database BitBankDB;
use BitBankDB;
USE BanksAccountsDB
DROP DATABASE BitbankDB;

CREATE TABLE Accounts(
	AccountID			bigint primary key identity, 
	AccountUsername		varchar(255) unique not null,
	AccountPassword		varchar(255) not null,
	AccountEmail		varchar(255) unique not null,
	AccountNip			int not null
);

CREATE TABLE Coins(
	CoinID		bigint primary key identity,
	CoinName	varchar(100) not null,
	CoinKey		varchar(5) not null,
	CoinImgPath	varchar(255) unique,
	CoinValue	bigint not null
);

CREATE TABLE Wallet(
    WalletID            bigint primary key identity,
    WalletAccountsID    bigint not null, -- FK
    WalletCoinID        bigint not null, -- FK
    WalletCoinQuantity    bigint not null,
    WalletBalance        bigint not null,
    constraint fk_wallet_accounts foreign key (WalletAccountsID) references Accounts(AccountID) on delete cascade,
    constraint fk_wallet_Coins    foreign key (WalletCoinID)     references Coins(CoinID) on delete cascade
);

CREATE TABLE ProfileAccounts(
	ProfileID			bigint primary key identity,
	ProfileName			varchar(255) not null,
	ProfileLastName		varchar(255) not null,
	ProfileNumberPhone	varchar(15) unique,
	ProfileAccountID	bigint unique,
	constraint fk_profileaccounts_accounts foreign key (ProfileAccountID) references Accounts(AccountID) on delete cascade
);

CREATE TABLE Transactions(
	TransactionID			bigint primary key identity,
	TransactionAmount		bigint not null,
	TransactionDate			time not null,
	TransactionReceiver		bigint not null,
	TransactionTransmitter	bigint not null,
	constraint fk_transactions_accounts1 foreign key (TransactionReceiver) references Accounts(AccountID) ON DELETE CASCADE,
	--constraint fk_transactions_accounts2 foreign key (TransactionTransmitter) references Accounts(AccountID) ON DELETE CASCADE NO ACTION
);

ALTER TABLE Transactions
ADD CONSTRAINT fk_transactions_accounts2 
FOREIGN KEY (TransactionTransmitter) 
REFERENCES Accounts(AccountID) 
ON DELETE NO ACTION;

CREATE Table AuditLogs(
	AuditLogID			bigint primary key identity,
	AuditLogAccount		bigint unique not null,
	AuditLogDescription	text not null,
	AuditLogTime		time,
	constraint fk_auditlog_accounts foreign key (AuditLogAccount) references Accounts(AccountID) on delete cascade
);