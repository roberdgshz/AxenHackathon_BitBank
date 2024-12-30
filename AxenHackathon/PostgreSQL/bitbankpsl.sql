--- Tables
CREATE TABLE Accounts(
	AccountID			bigint primary key generated always as identity, 
	AccountUsername		varchar(255) unique not null,
	AccountPassword		varchar(255) not null,
	AccountEmail		varchar(255) unique not null,
	AccountNip			int not null
);

CREATE TABLE Coins(
	CoinID		bigint primary key generated always as identity,
	CoinName	varchar(100) not null,
	CoinKey		varchar(5) not null,
	CoinImgPath	varchar(255) unique,
	CoinValue	bigint not null
);

CREATE TABLE Wallet(
	WalletID			bigint primary key generated always as identity,
	WalletBalance		bigint not null,
	WalletAccountsID	bigint unique not null,
	WalletCoinsID		bigint unique not null,
	constraint fk_wallet_accounts foreign key (WalletAccountsID) references Accounts(AccountID) on delete cascade
);

CREATE TABLE WalletCoins(
	WalletCoinID 			bigint primary key generated always as identity,
	WalletCoinQuantity		bigint not null,
	WalletCoinWalletID		bigint unique not null,
	constraint fk_walletcoins_wallet foreign key  (WalletCoinWalletID) references Wallet(WalletID) on delete cascade
);

CREATE TABLE ProfileAccounts(
	ProfileID			bigint primary key generated always as identity,
	ProfileName			varchar(255) not null,
	ProfileLastName		varchar(255) not null,
	ProfileNumberPhone	varchar(15) unique,
	ProfileAccountID	bigint unique,
	constraint fk_profileaccounts_accounts foreign key (ProfileAccountID) references Accounts(AccountID) on delete cascade
);

CREATE TABLE Transactions(
	TransactionID			bigint primary key generated always as identity,
	TransactionAmount		bigint not null,
	TransactionDate			time not null,
	TransactionReceiver		bigint not null,
	TransactionTransmitter	bigint not null,
	constraint fk_transactions_accounts1 foreign key (TransactionReceiver) references Accounts(AccountID) on delete cascade,
	constraint fk_transactions_accounts2 foreign key (TransactionTransmitter) references Accounts(AccountID) on delete cascade
);

CREATE Table AuditLogs(
	AuditLogID			bigint primary key generated always as identity,
	AuditLogAccount		bigint unique not null,
	AuditLogDescription	text not null,
	AuditLogTime		time,
	constraint fk_auditlog_accounts foreign key (AuditLogAccount) references Accounts(AccountID) on delete cascade
);

--- Foreign keys
alter table Wallet add constraint fk_wallet_walletcoins foreign key (WalletCoinsID) references WalletCoins(WalletCoinID) on delete cascade;

--- Indexs
CREATE UNIQUE INDEX idx_email_unique ON Accounts (AccountEmail);