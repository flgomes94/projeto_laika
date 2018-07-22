package com.laika.miaudota.comunicacao;

import com.laika.miaudota.models.Animal;

public interface IComunicacao {

    boolean cadastrar(Animal animal);
    boolean atualizar(Animal animal);
    boolean deletar(Animal animal);
    Animal listar();







}