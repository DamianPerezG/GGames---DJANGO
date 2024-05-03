@PostMapping(value = "/quitar/{indice}")
public String quitarDelCarrito(@PathVariable int indice, HttpServletRequest request) {
    ArrayList<ProductoParaVender> carrito = this.obtenerCarrito(request);
    if (carrito != null && carrito.size() > 0 && carrito.get(indice) != null) {
        carrito.remove(indice);
        this.guardarCarrito(carrito, request);
    }
    return "redirect:/vender/";
}