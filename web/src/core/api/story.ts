// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { resolveServiceURL } from "./resolve-service-url";

export interface GenerateStoryRequest {
  idea: string;
  outline?: string;
  partial_draft?: string;
}

export interface GenerateStoryResponse {
  story: string;
  outline: string;
  critique: string;
}

export async function generateStory(
  req: GenerateStoryRequest,
): Promise<GenerateStoryResponse> {
  const response = await fetch(resolveServiceURL("story/generate"), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req),
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return (await response.json()) as GenerateStoryResponse;
}
