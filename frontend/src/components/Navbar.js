import { React } from "react";
import { Link } from "react-router-dom";

export const Navnar = () => (
    <nav>
        <Link className="navbar-togglers" to="/"> Contratacion Maestros</Link>
        <button className="navbar-togglers" type="button" data-toggle="collapse"></button>
    </nav>
)