Algoritmo AgenciaDeCambio
	Definir COP Como Real;
	Definir conversion Como Caracter;
	
	COP<-0;
	conversion<-"";
	moneda_salida<-0;
	
	Escribir ("Digite la cantidad en COP que desea ingresar");
	Leer COP;
	
	Escribir ("Digite la moneda que desea convertir (USD - EUR)");
	Leer conversion;
	
	Si conversion = "USD" Entonces
		COP <- COP / 4060;
	SiNo
		Si conversion = "EUR" Entonces
			COP <- COP / 4433;
		FinSi
		Escribir ("Opcion incorrecta")
	Fin Si
	
	Escribir COP
	
FinAlgoritmo
