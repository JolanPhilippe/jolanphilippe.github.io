(* From: HPCS 2017 - Tutorial                          *)
(* http://frederic.loulergue.eu/hpcs2017               *)

Section Examples.

  Parameters A B C : Prop.

  Lemma proof1:
    A->B->(A->C)->(B->C)->C.
  Proof.
    intro HA.
    intro HB.
    intro HAC.
    Show Proof.
    intro HBC.
    apply HBC.
    assumption.
  Qed.

  Lemma proof2:
    A->B->(A->C)->(B->C)->C.
  Proof.
    intros HA HB HAC HBC.
    apply HBC.
    assumption.
  Qed.
  
  Print proof1.
  
  Print proof2.
  
  Definition proof3:
    forall (A B C:Prop),A->B->(A->C)->(B->C)->C :=
    fun A B C HA HB HAC HBC => (HAC HA).
  
  Definition proof4:
    forall (A B C:Prop),A->B->(A->C)->(B->C)->C.
  Proof.
    auto.
  Qed.

End Examples.


