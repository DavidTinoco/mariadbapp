%include('header.tpl')
                        <h3>Introduzca sus datos y elija la tabla a consultar.</h3>
                        <form action="select" method="post">
                                <label> Usuario: </label>
                                <input type="text" name="user" required/>
                                <label> Contraseña: </label>
                                <input type="password" name="key" required/>
                        <label>Tabla:</label>
                        <select name= "table">
                                <option selected value="0">Elija una tabla</option>
                                <option value="clientes">Clientes</option>
                                <option value="pedidos">Pedidos</option>
                                <option value="personas">Personas</option>
                        </select>
                        <input type="submit" value="Go">
                        </form>
%include('footer.tpl')
