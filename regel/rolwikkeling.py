def    rol_wikkeling_matches(rwid: int) -> str:
    match rwid:
        case 1:
            return "geen Rolwikkeling"
        case 2:
            return "Rolwikkeling 1"
        case 3:
            return "Rolwikkeling 2"
        case 4:
            return "Rolwikkeling 3"
        case 5:
            return "Rolwikkeling 4"
        case 6:
            return "Rolwikkeling 5"
        case 7:
            return "Rolwikkeling 6"
        case 8:
            return "Rolwikkeling 7"
        case 9:
            return "Rolwikkeling 8"
        case 10:
            return "Rolwikkeling diversen"


if __name__ == "__main__":
    print(rol_wikkeling_matches(3))
