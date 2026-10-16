def registrar_pago(pagos, referencia, monto_centimos):
    if not referencia.strip():
        raise ValueError("La referencia no puede estar vacía")
    if monto_centimos <= 0:
        raise ValueError("El monto debe ser positivo")
    if referencia in pagos:
        return False

    pagos[referencia] = monto_centimos
    return True
