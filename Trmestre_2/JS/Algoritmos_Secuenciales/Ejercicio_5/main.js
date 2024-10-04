let Compra = 20000;

let Descuento = Compra * 0.10;
let valorDescuento = Compra - Descuento;
let Iva = valorDescuento * 0.19;
let Total = valorDescuento + Iva;

console.log(`Iva: ${Iva}`);
console.log(`Valor total de la factura: ${Total}`);