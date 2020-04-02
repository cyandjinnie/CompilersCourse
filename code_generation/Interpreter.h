#pragma once
#include "Visitor.h"

class Interpreter : public Visitor {
 public:
  Interpreter();

  void Visit(AddExpr* that) override;
  void Visit(SubExpr* that) override;
  void Visit(MulExpr* that) override;
  void Visit(DivExpr* that) override;

 private:
  
};
