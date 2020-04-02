#pragma once
#include "Visitor.h"

class PrintVisitor : public Visitor {
 public:
  PrintVisitor();

  void Visit(AddExpr* that) override;
  void Visit(SubExpr* that) override;
  void Visit(MulExpr* that) override;
  void Visit(DivExpr* that) override;

 private:
  
};
