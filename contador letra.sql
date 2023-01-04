--Cuenta las letras de una palabra
declare		@nombre1	varchar(10),
			@nombre2	varchar(10),
			@longitud1	int,
			@longitud2	int,
			@letra		varchar(1),
			@contador	int,
			@sql		nvarchar(2000)

set @nombre1='martha'
set @nombre2='marta'
set @contador=1

select @longitud1=LEN(@nombre1)
select @longitud2=LEN(@nombre2)
set @sql='create table nombre( '

while @contador<=@longitud1
begin
	set @letra=LEFT(@nombre1,1)
	set @nombre1=RIGHT(@nombre1,LEN(@nombre1)-1)
	set @sql=@sql+@letra+cast(@contador as varchar(1))+' int, '
	set @contador=@contador+1
end
set @sql=LEFT(@sql,LEN(@sql)-1)
set @sql=@sql+')'

EXECUTE sp_executesql @sql

print @sql