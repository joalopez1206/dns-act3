## Pasos para resolver esta actividad!
1. Crear un archivo `resolver.py` la funcion de este modulo es que nos permita obtener
mensajes DNS asociado a `('localhost', 8000)` (__USAR SOCKET UDP__).
   - Luego haga que su socket pueda recibir mensajes en un loop, aquí puede utilizar un tamaño de buffer "grande"
   pues en esta actividad no nos preocuparemos de manejar mensajes más grandes que el tamaño del buffer. 
   - Finalmente haga que su código imprima en pantalla el mensaje recibido tal como se recibió, 
   es decir, no utilice `decode()`.
2. Programar una funcion para parsear mensajes DNS. Es decir
    - hay que programar una funcion que tome un mensaje DNS y me retorne el
   DNS en una estructura de datos manejable.
      - _HINT_: se recomienda guardar los siguientes datos.
        - `QNAME`
        - `ANCOUNT`
        - `NSCOUNT`
        - `ARCOUNT`
        - Seccion Answer.
        - Seccion Authority.
        - Seccion Additional.
