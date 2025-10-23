// ConsultaRepository.java
package com.consultorio.repository;
import com.consultorio.model.Consulta;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ConsultaRepository extends JpaRepository<Consulta, Long> {

    
}